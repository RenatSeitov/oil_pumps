"""users

Revision ID: 8b3d16ef0b60
Revises: 360d611eaab9
Create Date: 2023-04-21 12:34:42.793450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b3d16ef0b60'
down_revision = '360d611eaab9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'UsersProfile',
        sa.Column('user_id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('fast_name', sa.String(), nullable=False),
        sa.Column('last_name', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
    )


def downgrade() -> None:
    pass
